import React, {useState, useEffect} from 'react'
import './SwitchEntry.js'

export default function SwitchEntry(switchInfo) {
   const [isOn, setIsOn] = useState(false)
   
   const updateStatus = () => {
    fetch(switchInfo.statusUrl)
    .then(dat => {setIsOn(dat); console.log(dat)})
   }
   
   // Mount and unmount functions
   useEffect(() => {
     let interval = setInterval(updateStatus, 1000)
     return () => {
         clearInterval(interval)
     }
   })

   
  return (
    <div>
        <h1>{switchInfo.name} - <div class="link">{isOn ? "On" : "Off"}</div></h1>
    </div>
  )
}
