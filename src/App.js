import SwitchEntry from './SwitchEntry';
import React, {useState, useEffect} from 'react'

function App() {
   const [SwitchList, setSwitchList] = useState([])

   useEffect(() => {
     let switchJSON = []
     fetch("http://localhost:3001/switches/")
      .then(dat => dat.json())
      .then(dat => {
        switchJSON = dat;
        console.log(dat);
        const entries = switchJSON.map(entry => {
          console.log(entry)
          return <SwitchEntry key={entry.name} switchInfo={entry} />
        }
        );
    setSwitchList(() => entries);
    return true
      })
    
    
     
   }, [])
   

  return (
    <div className="App">
      {SwitchList}
    </div>
  );
}

export default App;
