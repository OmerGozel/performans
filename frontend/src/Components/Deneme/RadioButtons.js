import {useState} from 'react';

export default function RadioButtons(){
    const [ratio, setRatio] = useState("threeToOne");

    function handleChange(e){
        setRatio(e.target.value)
    }
    return (
             <div>
                <div className='radio'>
                            <label>
                            <input name="ratioRadio" 
                            type="radio"  
                            value={"threeToOne"}
                            checked = {ratio === "threeToOne"} 
                            onChange={handleChange}
                            /> Üç Yanlış Bir Doğru götürür.
                            </label>
                        </div>
                        <div className='radio'>
                            <label>    
                            <input name="ratioRadio"
                            type="radio" 
                            value={"fourToOne"}
                            checked = {ratio === "fourToOne"}
                            onChange={handleChange} 
                            /> Dört Yanlış Bir doğru götürür.
                            </label>
                        </div>
                        <div className='radio'>
                            <label>
                            <input name="ratioRadio"
                            type="radio" 
                            value={"noEffect"}
                            checked= {ratio === "noEffect"} 
                            onChange={handleChange}
                            /> Yanlışların etkisi yok.
                            </label>
                 </div>
           </div>
    )
 }