import SwitchEntry from './SwitchEntry';
import React, {useState, useEffect} from 'react'

function App() {
   const [SwitchList, setSwitchList] = useState([])

  //Fetch the list of switches
   useEffect(() => {
     fetch("http://localhost:3001/switches/")
      .then(dat => dat.json())
      .then(dat => setSwitchList(dat))  
   }, [])
   

  return (
    <div className="App">
      {SwitchList && SwitchList.map(entry => 
        <SwitchEntry key={entry.name} switchInfo={entry} />
      )}
    </div>
  );
}

export default App;
