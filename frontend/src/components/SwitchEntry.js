import React, {useState, useEffect} from 'react'
import './SwitchEntry.css'
import classNames from 'classnames'

export default function SwitchEntry({switchInfo}) {
   const [isOn, setIsOn] = useState(false)
   const [Connected, setConnected] = useState(true)

   const fetchUrl = (url) => {
    fetch(url)
    .then(dat => dat.json())
    //Set the data and set the connected fl
    .then(dat => {setIsOn(dat.status); setConnected(true)})
    .catch(() => setConnected(false))
   }
   
   // Mount and unmount functions
   useEffect(() => {
     fetchUrl(switchInfo.status_url);
     let interval = setInterval(() => fetchUrl(switchInfo.status_url), 3000)
     return () => {
         clearInterval(interval)
     }
   })

   
  return (
    <div className="card m-2">
      <div className="card-body row align-items-center">
      <div className="col-10 align-middle ">
        <a href={"/switch/"+switchInfo.slug}>
          <h1 className="display-4">
          {switchInfo.name}
          </h1>
        </a>
        </div>
        <div className="col-2">
          {(Connected ?
          (<img src="/power-svgrepo-com.svg" 
                alt="" 
                width="100%" 
                className={classNames({on: isOn, link:true})}
                onClick={() => fetchUrl(switchInfo.toggle_url)}
                ></img>) :
          ("Disconnected")
          )}
        </div>
      </div>

    </div>
  )
}
