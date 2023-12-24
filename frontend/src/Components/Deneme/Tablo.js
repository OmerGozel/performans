import { dersler as dersAdlari} from '../Data';


export default function Tablo({dersler}) {
    let net, top, t_dogru=0, t_yanlis=0, t_bos= 0, t_net = 0, t_top= 0;
    
    let rows = [];
     
    for (let ders of dersler)
    {
      /*if (Object.keys(ders).indexOf('id') <0)
      {
        continue;
      }*/
      net = (+ders.dogru - +ders.yanlis / 3.0).toFixed(2);
      top = (+ders.dogru + +ders.yanlis + +ders.bos);
      
      t_dogru = +t_dogru + +ders.dogru;
      t_yanlis = +t_yanlis + +ders.yanlis;
      t_bos = +t_bos + +ders.bos;
      t_net = (+t_dogru - + t_yanlis / 3.0).toFixed(2);
      t_top = t_dogru + t_yanlis + t_bos;
      
      rows = [...rows,<tr key = {ders.id}>
              <td>{(dersAdlari.find(d=> d.value === ders.id)).label}</td>
              <td>{ders.dogru}</td>
              <td>{ders.yanlis}</td>
              <td>{ders.bos}</td>
              <td>{net}</td>
              <td>{top}</td>
             </tr>];
    }

  return (
    
    <div>
      {rows.length > 0 &&
      <table className ="table table-bordered">
       <thead>
        <tr>
          <th>Ders</th>
          <th>Doğru</th>
          <th>Yanlış</th>
          <th>Boş</th>
          <th>Net</th>
          <th>Top</th>
      </tr>
    </thead>
    <tbody>
              {rows}
              
              <tr className='font-weight-bold'>
              <td>Toplam</td>
              <td>{t_dogru}</td>
              <td>{t_yanlis}</td>
              <td>{t_bos}</td>
              <td>{t_net}</td>
              <td>{t_top}</td>
              </tr>
       </tbody>
      </table>}
    </div>
  )
}
