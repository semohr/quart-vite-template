import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
    plugins: [react()],
    server: {
        /** Allow the api calls to be
         * made to the another port during
         * development as the frontend and
         * backend are running independently
         * in dev.
         *
         * For production, the frontend and
         * backend are served from the quart
         * app, so the api calls are made
         * to and from the same port.
         */
        proxy: {
            "^/api_v1/.*": {
                target: "https://github.com/",
                changeOrigin: true,
            },
        },
    },
});
