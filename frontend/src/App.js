import SwitchEntry from './SwitchEntry';
import React, {useState, useEffect} from 'react'
import './App.css'

function App() {
   const [SwitchList, setSwitchList] = useState([])

  //Fetch the list of switches
   useEffect(() => {
     fetch("http://localhost:8000/switches/")
      .then(dat => dat.json())
      .then(dat => setSwitchList(dat))  
   }, [])
   

  return (
    <div className='container'>
      <div className="row justify-content-center">
        <div className="col-lg-6">
          {SwitchList && SwitchList.map(entry =>
            <SwitchEntry key={entry.name} switchInfo={entry} />
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
