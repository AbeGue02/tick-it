import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'


export default function EventDetails() {

    const { eventId } = useParams()
    const [events, setEvents] = useState([])
    const [numOfTickets, setNumOfTickets] = useState(1)
    let navigate = useNavigate()

    const getEventDetail = async () => {
        let response = eventId ? 
            await axios.get(`http://localhost:8000/events/${eventId}`) : 
            await axios.get('http://localhost:8000/events')
        setEvents(response.data)
        console.log(response.data)
    }

    const deleteEvent = async () => {
        let response = await axios.delete(`http://localhost:8000/events/${eventId}`)
        console.log(response)
        navigate('/events')
    }

    useEffect(() => {
        getEventDetail()
    }, [])


    return (
        <div className='eventsDetailsContainer'>
            <img className='event-image' src={events.event_img} alt="" />
            <h3>{events.name} @ {new Date(events.date).toLocaleString()}</h3>
            <h4>{events.venue_name}</h4>
            <h4>{events.event_city}, {events.event_state}</h4>
            <iframe style={{border: 0, width: '100%'}} loading="lazy" allowFullScreen src={`https://www.google.com/maps/embed/v1/search?q=${`${events.venue_name}%2C%20${events.event_city}%2C%20${events.event_state}`}&key=${import.meta.env.VITE_GOOGLE_MAPS_API_KEY}`}></iframe>
            <h3>{events.seating_type}</h3>
            <h3>${events.cost * numOfTickets}</h3>
            <input type='number' value={numOfTickets} onChange={(e) => setNumOfTickets(e.target.value)} defaultValue={1} min={1} max={10}/>

            <button className='checkoutButton' onClick={() => navigate('/checkout')}>Checkout</button>

            <button 
                className='deleteButton'
                onClick={deleteEvent}>Delete Event</button>

        </div>
    )
}