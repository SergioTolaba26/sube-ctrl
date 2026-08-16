import { defineConfig } from 'vite'
import fs from 'fs'

export default defineConfig({
    server: {
        host: true,
        https: {
            key: fs.readFileSync('./localhost+2-key.pem'),
            cert: fs.readFileSync('./localhost+2.pem'),
        },
    },
})