import react from '@vitejs/plugin-react-swc'
import path from 'path';
import {defineConfig} from 'vite'

// https://vite.dev/config/
export default defineConfig({
  server: {
    host: '::',
    port: 8080
  },  // bind the development server to run on port 8080
  plugins: [react()],
  resolve: {
    alias: {'@': path.resolve(__dirname, './src')}
  }  // create a shortcut to import file using @/
})
