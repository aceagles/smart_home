import React, {useState, useEffect} from 'react'
import './SwitchEntry.css'

export default function SwitchEntry({switchInfo}) {
   const [isOn, setIsOn] = useState(false)
   const [Connected, setConnected] = useState(true)

   const updateStatus = () => {
    fetch(switchInfo.statusUrl)
    .then(dat => dat.json())
    //Set the data and set the connected fl
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
    <div className="card m-2">
      <div className="card-body row align-items-center">
        <div className="col-10 align-middle ">{switchInfo.name} - </div>
        <div className="col-2">
          {(Connected ?
          (<img src="/power-svgrepo-com.svg" alt="" width="100%" className={(isOn ? "on" : "")}></img>) :
          ("Disconnected")
          )}
        </div>
      </div>

    </div>
  )
}
