import Overview from './routes/overview'
import React, {useEffect} from 'react'
import './App.css'
import {useDispatch } from 'react-redux'
import {setSwitches} from './store/switches/switchSlice'
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {
  const dispatch = useDispatch()

  //Fetch the list of switches
   useEffect(() => {
     fetch("http://localhost:8000/switches/")
      .then(dat => dat.json())
      .then(dat => dispatch(setSwitches(dat)))  
   })
   

  return (
    <Router>
      <Routes>
          <Route path="/" element={<Overview />}/>
          
        </Routes>
    </Router>
  );
}

export default App;
