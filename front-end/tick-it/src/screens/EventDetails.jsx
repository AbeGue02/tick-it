import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { Link } from 'react-router-dom'
import axios from 'axios'

export default function EventDetails() {

    const { eventId, venueId } = useParams()
    const [events, setEvents] = useState([])
    const [venues, setVenues] = useState([])

    const getEventDetail = async () => {
        let response = eventId ? 
            await axios.get(`http://localhost:8000/events/${eventId}`) : 
            await axios.get('http://localhost:8000/events')
        setEvents(response.data)
        console.log(response.data)
    }

    useEffect(() => {
        getEventDetail()
    }, [])

    
    return (
        <div className='eventsDetailsContainer'>
            <img className='event-image' src={events.event_img} alt="" />
            <h2>{events.name} @ {new Date(events.date).toLocaleString()}</h2>
            <h3>{events.venue_name}</h3>
            <h3>{events.event_city}, {events.event_state}</h3>
            <h3>{events.seating_type}</h3>
            <h3>${events.cost}</h3>
            <Link to='/checkout'><button> Checkout </button></Link>
        </div>
    )
}