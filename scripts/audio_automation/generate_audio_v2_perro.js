require('dotenv').config();
const fs = require('fs');
const path = require('path');
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
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    console.error('Falta GEMINI_API_KEY en scripts/audio_automation/.env');
    process.exit(1);
  }

  const scriptPath = path.join(PROJECT_ROOT, 'scripts', 'day_01', 'video_04_evolucion_perro_v2.md');
  const outPath = path.join(PROJECT_ROOT, 'assets', 'day_01', 'audio_notes', 'video_04_narration_v2.wav');

  const scriptText = fs.readFileSync(scriptPath, 'utf8');
  const narration = extractNarration(scriptText);
  if (!narration) {
    console.error('No se encontro seccion "Voz o narracion sugerida" en el guion v2');
    process.exit(1);
  }

  const ai = new GoogleGenAI({ apiKey });
  console.log(`Generando narracion v2 (${narration.length} caracteres) con voz ${VOICE} / modelo ${MODEL}...`);
  await generateNarration(ai, narration, outPath);
  console.log('Guardado en ' + path.relative(PROJECT_ROOT, outPath));
}

main().catch((err) => {
  console.error('ERROR:', err.message);
  process.exit(1);
});
