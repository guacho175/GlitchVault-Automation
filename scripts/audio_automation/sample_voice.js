require('dotenv').config();
const path = require('path');
const wav = require('wav');
const { GoogleGenAI } = require('@google/genai');

const MODEL = process.env.GEMINI_TTS_MODEL || 'gemini-2.5-flash-preview-tts';

function saveWaveFile(filename, pcmData, channels = 1, rate = 24000, sampleWidth = 2) {
  return new Promise((resolve, reject) => {
    const writer = new wav.FileWriter(filename, { channels, sampleRate: rate, bitDepth: sampleWidth * 8 });
    writer.on('finish', resolve);
    writer.on('error', reject);
    writer.write(pcmData);
    writer.end();
  });
}

async function main() {
  const voice = process.argv[2];
  const text = process.argv[3];
  const outPath = process.argv[4];
  const apiKey = process.env.GEMINI_API_KEY;

  if (!voice || !text || !outPath) {
    console.error('Uso: node sample_voice.js <voz> "<texto>" <archivo_salida.wav>');
    process.exit(1);
  }

  const ai = new GoogleGenAI({ apiKey });
  const response = await ai.models.generateContent({
    model: MODEL,
    contents: [{ parts: [{ text }] }],
    config: {
      responseModalities: ['AUDIO'],
      speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: voice } } },
    },
  });

  const part = response.candidates?.[0]?.content?.parts?.[0];
  const audioData = part?.inlineData?.data;
  if (!audioData) throw new Error('Sin audio en la respuesta: ' + JSON.stringify(response).slice(0, 500));

  const pcmBuffer = Buffer.from(audioData, 'base64');
  await saveWaveFile(outPath, pcmBuffer);
  console.log(`OK: ${voice} -> ${outPath}`);
}

main().catch((e) => { console.error(e.message); process.exit(1); });
