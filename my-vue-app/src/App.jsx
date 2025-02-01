import { useState } from 'react'
import './App.css'
import Action from './Modules/action/action'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <Action />
    </>
  )
}

export default App
