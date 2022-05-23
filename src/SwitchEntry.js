import React, {useState, useEffect} from 'react'
import './SwitchEntry.css'

export default function SwitchEntry({key, switchInfo}) {
   const [isOn, setIsOn] = useState(false)
   const updateStatus = () => {
    fetch(switchInfo.statusUrl)
    .then(dat => dat.json())
    .then(dat => {setIsOn(dat.status)})
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
      {switchInfo.name} - <div className="link">{isOn ? "On" : "Off"}</div>
    </div>
  )
}
