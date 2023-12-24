import { useState } from 'react';
import {Denemeler} from "../Data";
import { dersler as dersAdlari } from '../Data';
import Select from 'react-select';
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'
import { useDispatch } from 'react-redux'
import { add } from '../../features/deneme/denemeSlice';
import { useImmer } from 'use-immer'

export default function Form({dersler, updateDersler}){
    const [deneme, updateDeneme]= useImmer({tarih:"",id: 0});
    const [date, setDate] = useState(null);
    const [selectedDenemeOption, setselectedDenemeOption] = useState(null);
    const [selectedDersOption, setselectedDersOption] = useState(null);
    const [ders, updateDers] = useImmer({id:0, dogru: 0, yanlis:0, bos: 0});
    const [button, setButton] = useState ({text:"Ekle", sil:false});
    const dispatch = useDispatch();

    function handleDateChange(date)
    {
      setDate(date);
      let _date = date.toLocaleDateString();
      updateDeneme(draft => {draft.tarih = _date});
    }

    function handleDenemeChange(selectedDenemeOption){
      setselectedDenemeOption(selectedDenemeOption);
      updateDeneme(draft => {draft.id = selectedDenemeOption.value})      
    }

    function handleSelectedDersChange(selectedDersOption){
      setselectedDersOption(selectedDersOption);
      
      for (let ders of dersler)
        {
          if(ders.id === selectedDersOption.value)
            {
              updateDers({id:ders.id, dogru:ders.dogru, yanlis:ders.yanlis,bos: ders.bos,})
              setButton({text:"Düzenle",sil:true});
              return;
            }
        }
      updateDers({id:selectedDersOption.value,dogru:0, yanlis:0, bos:0,});
      setButton({text:"Ekle", sil:false});
      
      //updateDers (draft => {draft.id = selectedDersOption.value})      
    }

    function handledogruChange(e){
      updateDers(draft => {draft.dogru = e.target.value});
    }

    function handleYanlisChange(e){
      updateDers(draft => {draft.yanlis = e.target.value});
    }

    function handleBosChange(e){
      updateDers(draft => {draft.bos = e.target.value});
    }
    
    function setToInitialValues(){
      updateDers({id: 0,dogru:0, yanlis:0, bos:0});
      setselectedDersOption(null);
      setButton({text:"Ekle", sil:false});
    }

    function handleEkleClick(e)
   {
     e.preventDefault();
     
     if(ders.id === 0)
       {
        alert("Lütfen ders seçimi yapınız!");
        return;
       }
      
       if(button.text === "Ekle")
       updateDersler(draft => {draft.push(ders)});
       
       else 
       {
        const _index = dersler.findIndex(d => (d.id === ders.id));
         
        updateDersler(draft =>{
          draft[_index].dogru = ders.dogru;
          draft[_index].yanlis = ders.yanlis;
          draft[_index].bos = ders.bos;
        })
        }
                  
      setToInitialValues();
   }

   function handleSilClick(){
    
    const yeniDersler = dersler.filter(d =>(d.id !== ders.id)); 
                       
     updateDersler(yeniDersler);
     setToInitialValues();
   }
   
    function handleKaydetClick ()
    {
      updateDeneme({...deneme,d:dersler}) 
      dispatch(add(deneme));
    }
    return (
         <>
                 <form >
                 <div style= {{ marginBottom:'20px'} }>
                 <DatePicker
                  showIcon={true}
                  selected={date} onChange={handleDateChange} 
                  dateFormat="dd/MM/yyyy"
                  placeholderText='Tarih'
                  />
                  </div>
                  <div>                 
                  <Select
                        value={selectedDenemeOption}
                        onChange={handleDenemeChange}
                        options={Denemeler}
                        placeholder= "Denemeler"
                    />
 
                  </div>
                  <div><hr/></div>
                  
                  <div className="form-group">
                    <Select
                        value={selectedDersOption}
                        onChange={handleSelectedDersChange}
                        options={dersAdlari}
                        placeholder= "Ders"
                    />
                    </div>
                  <hr/>  

                  <div className="input-group mb-3">
                             <div className="input-group-prepend">
                                 <span className="input-group-text" style = {{paddingRight:"18px"}}>Doğru :</span>
                             </div>
                             <input className="form-control" 
                               name='dogru'
                               type="number"
                               value={ders.dogru} 
                               onChange={handledogruChange}
                             />
                     </div>
                    
                     <div className="input-group mb-3">
                             <div className="input-group-prepend">
                                 <span className="input-group-text" style = {{paddingRight:"23px"}}
                                 >Yanlış :</span>
                             </div>
                             <input className="form-control"
                               name='yanlis'
                               type="number"
                               value={ders.yanlis}
                               onChange={handleYanlisChange}
                               />
                     </div>
                     <div className="input-group mb-3">
                             <div className="input-group-prepend">
                                 <span className="input-group-text" style = {{paddingRight:"37px"}}>
                                     Boş :</span>
                             </div>
                             <input className="form-control"
                               name='bos'
                               type="number"  
                               value={ders.bos}
                               onChange={handleBosChange}
                               />
                     </div> 

                                          {button.sil && <button type="button" className="btn btn-danger"
                     style={{float:"left", width: '48%'}} 
                     onClick={handleSilClick}
                     >Sil</button>}

                     <button type="button" className="btn btn-success" onClick={handleEkleClick}
                     style={{float:"right", width:"48%"}} 
                     
                     >{button.text}</button>
                    
                     
                    <button type="button" className="btn btn-success" onClick={handleKaydetClick}
                      style={{float:"right",width: '100%',
                              marginTop:"20px",
                              
                            }} 
                     
                     >Kaydet</button>
 
              </form>
         </>
     );
  }
                         