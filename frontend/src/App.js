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
    <div className='row'>
      <div className="column equal">&nbsp; </div>
      <div className="App column equal">
        {SwitchList && SwitchList.map(entry =>
          <SwitchEntry key={entry.name} switchInfo={entry} />
        )}
      </div>
      <div className="column equal"> &nbsp;</div>
    </div>
  );
}

export default App;
