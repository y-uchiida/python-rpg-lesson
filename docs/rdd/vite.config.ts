import { defaultTheme } from '@sveltepress/theme-default'
import { sveltepress } from '@sveltepress/vite'
import { defineConfig } from 'vite'
import { NAVBAR } from './src/constants/NAVBAR'
import { SIDEBAR } from './src/constants/SIDEBAR'

const config = defineConfig({
	server: {
		port: 5573,
	},
	plugins: [
		sveltepress({
			theme: defaultTheme({
				sidebar: SIDEBAR,
			}),
			siteConfig: {
				title: 'Python でつくるコマンドラインRPG',
			},
		}),
	],
})

export default config
