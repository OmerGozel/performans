import React, {useContext, useState, useEffect} from 'react'
import AuthContext from '../context/AuthContext'
import axios from 'axios';

export default function DenemePage() {
  
  const [denemeler, setDenemeler] = useState([]);
  const { authTokens, logoutUser } = useContext(AuthContext);


     async function fetchDenemeler (){

      let response = await fetch('http://127.0.0.1:8000/denemeler', {
        method: 'GET',
        headers:{
            'Content-Type': 'application/json',
            'Authorization':'Bearer ' + String(authTokens.access)
        }
        })
        
        let data = await response.json()
        
        if(response.status === 200){
            setDenemeler(data)
        } else if(response.statusText === 'Unauthorized'){
            logoutUser()
        }
       }

     useEffect(() => {
      fetchDenemeler();
     },[])

  
    return (
    <div>
      <ul>
      
      {
      denemeler.map((deneme) => (
       <li key={deneme.id}>{deneme.adi}</li>
      ))
      
    }
    </ul>
    </div>
  )
}
