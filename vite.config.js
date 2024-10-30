import { defineConfig } from 'vite';
import path from 'path';
import fs from 'fs';

const characterHtmlFiles = fs.readdirSync(path.resolve(__dirname, 'src/characters'))
    .filter(file => file.endsWith('.html'))
    .reduce((acc, file) => {
        const name = file.replace('.html', '');
        acc[name] = path.resolve(__dirname, `src/characters/${file}`);
        return acc;
    }, {});

export default defineConfig({
    root: path.resolve(__dirname, 'src'), // Configura 'src' como la raíz del proyecto
    build: {
        rollupOptions: {
            input: {
                main: path.resolve(__dirname, 'src/index.html'), // Indica el archivo HTML principal
                characters: path.resolve(__dirname, 'src/Characters.html'), // Otros archivos HTML que quieras construir
                banners: path.resolve(__dirname, 'src/banners_cn.html'),   // Añadir otros puntos de entrada si es necesario
                ...characterHtmlFiles
            }
        },
        outDir: path.resolve(__dirname, 'dist') // Define el directorio de salida
    }
});
