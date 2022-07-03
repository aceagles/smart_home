import React, {useEffect} from 'react'
import './App.css'
import {useDispatch } from 'react-redux'
import {setSwitches} from './store/switches/switchSlice'
import Overview from './routes/overview'
import Detail from './routes/Detail'



import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {
  const dispatch = useDispatch()

  //Fetch the list of switches
   useEffect(() => {
     fetch("/switches/")
      .then(dat => dat.json())
      .then(dat => dispatch(setSwitches(dat)))  
   })
   

  return (
    <Router>
      <Routes>
          <Route path="/" element={<Overview />}/>
          <Route path="/switch/:slug" element={<Detail />} />
        </Routes>
    </Router>
  );
}

export default App;
