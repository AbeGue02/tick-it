import axios from 'axios'
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'

export default function EventListItem({event}) {
    
    const [venue, setVenue] = useState({})

    let navigate = useNavigate()

    const getVenue = async () => {
        let response = await axios.get(event.venue)
        console.log(response.data)
        setVenue(response.data)
    }

    useEffect(() => {
        getVenue()
        console.log(event)
    }, [])

    return (
        <div 
            className='eventListItemContainer' 
            style={{backgroundImage: `linear-gradient(rgba(0,0,0,0.0), rgba(0,0,0,0.7)), url(${event.event_img})`}}
            onClick={() => navigate(`/events/${event.id}`)}
            >
            <h3>{event.name}</h3>
            <h5>{venue.name} @ {new Date(event.date).toLocaleString()}</h5>
            <h6>${event.cost}</h6>
        </div>
    )

}