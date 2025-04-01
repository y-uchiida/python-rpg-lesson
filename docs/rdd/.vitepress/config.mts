import { defineConfig } from 'vitepress';
import { NAVBAR } from '../src/constants/NAVBAR';
import { SIDEBAR } from '../src/constants/SIDEBAR';

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Python でつくるコマンドラインRPG",
  description: "Python で 簡易的な RPG 実装するハンズオン教材",
  srcDir: "src/routes",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    // nav: [
    //   { text: 'Home', link: '/' },
    //   { text: 'Examples', link: '/markdown-examples' }
    // ],
    nav: NAVBAR,

    sidebar: SIDEBAR,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
