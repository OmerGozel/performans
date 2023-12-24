import React,{ useContext } from 'react'
import { Link } from 'react-router-dom'
import AuthContext from '../context/AuthContext'

export default function Header() {
  
  let {user, logoutUser } = useContext(AuthContext);

  return (
    <nav className="navbar navbar-expand-sm bg-dark navbar-dark">
  {/*<!-- Brand -->*/}
  

  {/*<!-- Links -->*/}
  <ul className="navbar-nav mr-auto">
    <li className="nav-item">
    <Link className="nav-link" to="/">Home</Link>
    </li>
    

    {/*<!-- Dropdown -->*/}
    <li className="nav-item dropdown">
      <a className="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
        Deneme
      </a>
      <div className="dropdown-menu">
        <Link className="dropdown-item" to="/deneme">Ekle</Link>
        <a className="dropdown-item" href="#">Link 2</a>
        <a className="dropdown-item" href="#">Link 3</a>
      </div>
    </li>
    
  </ul>
    
  <div className="navbar-text  mr-sm-2">
  {
         user ? (
                  <span className = "nav-link" onClick={logoutUser}><a href='#'>Logout</a> | {user && user.username}</span>
                        ) : (
                            <Link className = "nav-link" to="/login" >Login</Link>
                        )
                        
  }
    
  </div>
   </nav>


  )
}
