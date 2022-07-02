import SwitchEntry from './SwitchEntry';
import React, {useEffect} from 'react'
import './App.css'
import { useSelector, useDispatch } from 'react-redux'
import {setSwitches} from './store/switches/switchSlice'

function App() {
  const SwitchList = useSelector(state => state.switches.switches)
  const dispatch = useDispatch()

  //Fetch the list of switches
   useEffect(() => {
     fetch("http://localhost:8000/switches/")
      .then(dat => dat.json())
      .then(dat => dispatch(setSwitches(dat)))  
   })
   

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
