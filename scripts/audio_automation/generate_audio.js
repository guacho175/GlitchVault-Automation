const path = require('path');
require('dotenv').config({ path: path.resolve(__dirname, '.env') });
const fs = require('fs');
const wav = require('wav');
const { GoogleGenAI } = require('@google/genai');

const PROJECT_ROOT = path.resolve(__dirname, '..', '..');
const VOICE = process.env.GEMINI_TTS_VOICE || 'Algenib';
const MODEL = process.env.GEMINI_TTS_MODEL || 'gemini-3.1-flash-tts-preview';

function extractNarration(scriptText) {
  const match = scriptText.match(/## Voz o narraci[oó]n sugerida\s*\n([\s\S]*?)(\n##\s|\n---|$)/);
  if (!match) return null;
  return match[1].trim();
}

function saveWaveFile(filename, pcmData, channels = 1, rate = 24000, sampleWidth = 2) {
  return new Promise((resolve, reject) => {
    const writer = new wav.FileWriter(filename, { channels, sampleRate: rate, bitDepth: sampleWidth * 8 });
    writer.on('finish', resolve);
    writer.on('error', reject);
    writer.write(pcmData);
    writer.end();
  });
}

async function generateNarration(ai, text, outPath) {
  const response = await ai.models.generateContent({
    model: MODEL,
    contents: [{ parts: [{ text }] }],
    config: {
      responseModalities: ['AUDIO'],
      speechConfig: {
        voiceConfig: { prebuiltVoiceConfig: { voiceName: VOICE } },
      },
    },
  });

  const part = response.candidates?.[0]?.content?.parts?.[0];
  const audioData = part?.inlineData?.data;
  if (!audioData) {
    throw new Error('La respuesta no trajo audio. Respuesta cruda: ' + JSON.stringify(response, null, 2).slice(0, 2000));
  }

  const pcmBuffer = Buffer.from(audioData, 'base64');
  await saveWaveFile(outPath, pcmBuffer);
}

async function main() {
  const day = (process.argv[2] || '01').padStart(2, '0');
  const onlyVideoId = process.argv[3]?.trim();
  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    console.error('Falta GEMINI_API_KEY. Crea scripts/audio_automation/.env con GEMINI_API_KEY=tu_key');
    process.exit(1);
  }

  const scriptsDir = path.join(PROJECT_ROOT, 'scripts', `day_${day}`);
  const audioDir = path.join(PROJECT_ROOT, 'assets', `day_${day}`, 'audio_notes');

  if (!fs.existsSync(scriptsDir)) {
    console.error(`No existe la carpeta ${scriptsDir}`);
    process.exit(1);
  }
  fs.mkdirSync(audioDir, { recursive: true });

  const scriptFiles = fs.readdirSync(scriptsDir)
    .filter((f) => f.endsWith('.md'))
    .filter((f) => !onlyVideoId || f.match(/^(video_\d+)/)?.[1] === onlyVideoId)
    .sort();
  if (scriptFiles.length === 0) {
    console.error(`No hay guiones .md${onlyVideoId ? ` para ${onlyVideoId}` : ''} en ${scriptsDir}`);
    process.exit(1);
  }

  const ai = new GoogleGenAI({ apiKey });

  for (const file of scriptFiles) {
    const videoId = file.match(/^(video_\d+)/)?.[1] || path.basename(file, '.md');
    const outPath = path.join(audioDir, `${videoId}_narration.wav`);

    if (fs.existsSync(outPath)) {
      console.log(`- ${videoId}: ya existe, se omite (borra el .wav para regenerar)`);
      continue;
    }

    const scriptText = fs.readFileSync(path.join(scriptsDir, file), 'utf8');
    const narration = extractNarration(scriptText);

    if (!narration) {
      console.warn(`- ${videoId}: no se encontro seccion "Voz o narracion sugerida", se omite`);
      continue;
    }

    try {
      console.log(`- ${videoId}: generando narracion (${narration.length} caracteres)...`);
      await generateNarration(ai, narration, outPath);
      console.log(`  guardado en ${path.relative(PROJECT_ROOT, outPath)}`);
    } catch (err) {
      console.error(`  ERROR generando ${videoId}:`, err.message);
    }
  }
}

main();
