import react from '@vitejs/plugin-react-swc'
import path from 'path';
import {defineConfig} from 'vite'

// https://vite.dev/config/
export default defineConfig({
  // bind the development server to run on port 8080
  server: {host: '::', port: 8080},
  plugins: [react()],
  // bind the development server to run on port 8080
  resolve: {alias: {'@': path.resolve(__dirname, './src')}}
})
