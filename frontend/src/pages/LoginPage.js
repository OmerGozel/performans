import React, {useContext} from 'react'
import AuthContext from '../context/AuthContext'

export default function LoginPage() {
  
  let {loginUser} = useContext(AuthContext);
  
  
return (
    <div className="container pt-5">
        <form onSubmit={loginUser}>
            
            <div className="input-group mb-3">
                             <div className="input-group-prepend">
                                 <span className="input-group-text" style = {{paddingRight:"18px"}}>username :</span>
                             </div>
                             <input className="form-control" 
                               name='username'
                               type="text"
                               placeholder="Enter username"
                               //value={ders.dogru} 
                               //onChange={handledogruChange}
                             />
                     </div>
            
                     <div className="input-group mb-3">
                             <div className="input-group-prepend">
                                 <span className="input-group-text" style = {{paddingRight:"18px"}}>password :</span>
                             </div>
                             <input className="form-control" 
                               name='password'
                               type="password"
                               placeholder="enter password"
                               //value={ders.dogru} 
                               //onChange={handledogruChange}
                             />
                     </div>
            
            <input type="submit"/>
        </form>
    </div>
)
}
