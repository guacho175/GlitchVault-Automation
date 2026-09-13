const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, BorderStyle,
} = require('docx');

const videos = [
  {
    n: '01',
    title: 'DEL MICHI AL DIOS COSMICO 🌌🐈',
    file: 'video_01_FINAL.mp4',
    serie: 'Evoluciones con IA',
    desc: 'Del michi al Dios cósmico 🌌🐈 ¿A qué nivel llegaría tu mascota? ¿Qué animal quieres ver evolucionar mañana? Comenta abajo y sígueme para no perderte la próxima evolución.',
    hashtags: '#aiart #evolucion #rpg #glitchvault #gaming #gatos #ia',
  },
  {
    n: '02',
    title: 'ES HORA DE SER EL MALO 💀',
    file: 'video_02_FINAL.mp4',
    serie: 'Elige tu personaje',
    desc: 'Es hora de ser el malo 💀 ¿Con qué villano destruyes el servidor? ¿Cuál de los tres destruiría el mundo más rápido? Déjalo en comentarios y sígueme para la próxima ruta maldita.',
    hashtags: '#elige #villano #gaming #glitchvault #horror #creepy #rpg',
  },
  {
    n: '03',
    title: 'EL TETRIS QUE ESTA VIVO 🧩👁️',
    file: 'video_03_FINAL.mp4',
    serie: 'Videojuegos que no existen',
    desc: 'El juego de puzzles que no deberías jugar a oscuras 🧩👁️ Si quieres más juegos malditos, sígueme en GlitchVault.',
    hashtags: '#weirdcore #gaming #misterio #glitchvault #tetris #creepy #bodyhorror',
  },
  {
    n: '04',
    title: 'MORTALIS, EL GUARDIAN DE LA BIBLIOTECA 📚⚔️',
    file: 'video_04_FINAL.mp4',
    serie: 'Bosses imposibles',
    desc: 'Cuando el nivel entero ES el jefe final 📚⚔️ ¿Le ganarías o desinstalas el juego? Comenta y sígueme para el próximo boss imposible.',
    hashtags: '#bossfight #rpg #fantasia #glitchvault #gaming #darksouls #epic',
  },
];

const children = [];

children.push(new Paragraph({
  text: 'GlitchVault — Descripciones para TikTok',
  heading: HeadingLevel.HEADING_1,
}));

children.push(new Paragraph({
  children: [
    new TextRun({ text: 'Día 3 · Cuenta: ', bold: true }),
    new TextRun({ text: '@GlitchVault_', bold: true }),
  ],
}));

children.push(new Paragraph({
  children: [
    new TextRun({ text: 'Bio sugerida: "🕹️ Cosas que no deberían existir. | IA × Videojuegos × Lo extraño"' }),
  ],
  spacing: { after: 300 },
}));

for (const v of videos) {
  children.push(new Paragraph({
    text: `Video ${parseInt(v.n, 10)} — ${v.title}`,
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 300 },
  }));

  children.push(new Paragraph({
    children: [
      new TextRun({ text: 'Archivo: ', bold: true }),
      new TextRun({ text: v.file }),
      new TextRun({ text: '    |    ' }),
      new TextRun({ text: 'Serie: ', bold: true }),
      new TextRun({ text: v.serie }),
    ],
  }));

  children.push(new Paragraph({
    children: [new TextRun({ text: 'Descripción lista para pegar:', bold: true })],
    spacing: { before: 150 },
  }));

  children.push(new Paragraph({
    children: [new TextRun({ text: v.desc })],
  }));

  children.push(new Paragraph({
    children: [new TextRun({ text: v.hashtags, italics: true })],
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 6, color: 'CCCCCC', space: 8 },
    },
    spacing: { after: 200 },
  }));
}

const doc = new Document({
  sections: [{
    properties: {
      page: { size: { width: 12240, height: 15840 } },
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  const out = '../../assets/day_03/day_03_descripciones_tiktok.docx';
  fs.writeFileSync(out, buf);
  console.log('written', out);
});
