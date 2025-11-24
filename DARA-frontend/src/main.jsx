import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'

// Mount the React app into the #root element in index.html
const container = document.getElementById('root')
if (!container) throw new Error('Root container not found in index.html')

const root = createRoot(container)
root.render(
	<StrictMode>
		<App />
	</StrictMode>
)


