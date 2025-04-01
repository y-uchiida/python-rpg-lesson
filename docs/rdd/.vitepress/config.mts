import { defineConfig } from 'vitepress';
import { NAVBAR } from '../src/constants/NAVBAR';
import { SIDEBAR } from '../src/constants/SIDEBAR';
import { withMermaid } from "vitepress-plugin-mermaid";

// https://vitepress.dev/reference/site-config
export default withMermaid({
  title: "Python でつくるコマンドラインRPG",
  description: "Python で 簡易的な RPG 実装するハンズオン教材",
  srcDir: "src/routes",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: NAVBAR,
    sidebar: SIDEBAR,
    aside: false,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ],
    mermaid: {
      // refer https://mermaid.js.org/config/setup/modules/mermaidAPI.html#mermaidapi-configuration-defaults for options
    },
    mermaidPlugin: {
      class: "mermaid", // set additional css classes for parent container 
    },
  }
});
