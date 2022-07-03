import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import "./Detail.css"
import SwitchEntry from "../components/SwitchEntry";

export default function Detail() {
    const {slug} = useParams()
    const Switch = useSelector(state => state.switches.switches)
                            .find(o => o.slug === slug)

    return (
        <div className='container'>
            { Switch &&
            <div className="row justify-content-center">
                <div className="col-lg-8">
                    
                    <SwitchEntry key={Switch.name} switchInfo={Switch} />
                    
                    <div className="border rounded p-2 m-2 ">
                        <h4>Scheduled Events</h4>
                

                    </div>
                </div>
            </div>
            }
        </div>
    )
}