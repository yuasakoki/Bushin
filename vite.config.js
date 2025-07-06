import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/static/',  // こうするとビルド結果でJS・CSSが /static/assets/... になる
  plugins: [vue()],
  build: {
    outDir: 'src/python/static', // Flaskのstaticフォルダに出力
    emptyOutDir: true,
  }
})
