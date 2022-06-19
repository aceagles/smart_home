import React, {useState, useEffect} from 'react'
import './SwitchEntry.css'

export default function SwitchEntry({switchInfo}) {
   const [isOn, setIsOn] = useState(false)
   const [Connected, setConnected] = useState(false)

   const updateStatus = () => {
    fetch(switchInfo.statusUrl)
    .then(dat => dat.json())
    //Set the data and set the connected flag
    .then(dat => {setIsOn(dat.status); setConnected(true)})
    .catch(() => setConnected(false))
   }
   
   // Mount and unmount functions
   useEffect(() => {
     updateStatus();
     let interval = setInterval(updateStatus, 3000)
     return () => {
         clearInterval(interval)
     }
   })

   
  return (
    <div className="switchBox">
      {switchInfo.name} - 
      {(Connected ?
      (<img src="/power-svgrepo-com.svg" alt="" width="10%" className={(isOn ? "on" : "")}></img>) :
      ("Disconnected")
      )}
    </div>
  )
}
