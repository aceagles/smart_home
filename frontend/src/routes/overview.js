import {useSelector} from 'react-redux'
import SwitchEntry from '../components/SwitchEntry';

export default function Overview(){
    const SwitchList = useSelector(state => state.switches.switches)

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