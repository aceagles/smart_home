import { useDispatch } from "react-redux"
import { setSwitches } from "../store/switches/switchSlice"

export default function SchedEntry({sched}){
    const dispatch = useDispatch()
    function deleteEntry(){
        fetch(`/event/${sched.pk}`, {method: 'DELETE'})
        .then(dat => dat.json())
        .then(dat => dispatch(setSwitches(dat)))
    }


    return (
        <div>
            <div className="d-flex">
                {sched.time} | {sched.action} |
                <button className="btn btn-info m-2">
                    Edit
                </button>
                <button className="btn btn-danger m-2" onClick={deleteEntry}>
                    Delete
                </button>
            </div>
            <hr />
        </div>
    )

}