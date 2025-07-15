import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";
import fse from "fs-extra";

export default defineConfig({
  base: "/static/",
  plugins: [
    vue(),
    {
      name: "copy-to-backend",
      closeBundle: async () => {
        const srcDir = path.resolve(__dirname, "dist/static/assets");
        const destDir = path.resolve(__dirname, "../backend/app/static/assets");

        try {
          await fse.emptyDir(destDir);
          await fse.copy(srcDir, destDir, { overwrite: true });
          console.log("✅ assets copied to backend/app/static/assets/");
        } catch (err) {
          console.error("❌ Failed to copy assets:", err);
        }

        const indexHtmlSrc = path.resolve(__dirname, "dist/static/index.html");
        const indexHtmlDestToTemplate = path.resolve(
          __dirname,
          "../backend/app/templates/index.html"
        );
        const indexHtmlDestToStatic = path.resolve(
          __dirname,
          "../backend/app/static/index.html"
        );
        try {
          await fse.copy(indexHtmlSrc, indexHtmlDestToTemplate, {
            overwrite: true,
          });
          await fse.copy(indexHtmlSrc, indexHtmlDestToStatic, {
            overwrite: true,
          });
          console.log(
            "✅ index.html copied to backend/app/static/ and backend/app/templates/"
          );
        } catch (err) {
          console.error("❌ Failed to copy index.html:", err);
        }
      },
    },
  ],
  build: {
    outDir: "dist/static",
    emptyOutDir: true,
  },
  server: {
    proxy: {
      "/api": "http://localhost:5000",
    },
  },
});
