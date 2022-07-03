import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import "./Detail.css"

export default function Detail() {
    const {slug} = useParams()
    console.log(slug)
    const Switch = useSelector(state => state.switches.switches)
                        .find(o => o.slug === slug)
    console.log(Switch)

    return JSON.stringify(Switch)
}