//import {useState} from 'react';
import Tablo from "./Tablo";
import Form from "./Form";
import { useImmer } from 'use-immer';

export default function Deneme(){
    //const [toplam, setToplam] = useState({dogru: 0, yanlis: 0, bos: 0, net:0, top:0});
      const [dersler, updateDersler] = useImmer([]);
    return(
        <div className="container pt-5">
        
        <h1>Deneme Giriş Ekranı</h1>
        <hr/>
        <div className="row">
            <div className="col-md-4">
                <Form dersler={dersler} updateDersler = {updateDersler}/>
            </div>
            <div className="col-sm-8">
               <Tablo dersler={dersler}/>
            </div>
        </div> 
        </div>
        
    );
}

