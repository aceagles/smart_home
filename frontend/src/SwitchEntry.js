import React, {useState, useEffect} from 'react'
import './SwitchEntry.css'

export default function SwitchEntry({switchInfo}) {
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
      {switchInfo.name} - 
      <img src="/power-svgrepo-com.svg" alt="" width="10%" className={(isOn ? "on" : "")}></img>
    </div>
  )
}
