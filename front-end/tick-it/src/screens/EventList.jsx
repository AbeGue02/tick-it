import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'
import SearchBar from '../components/SearchBar'
import EventListItem from '../components/EventListItem'

export default function EventList() {
    // Lists all the events (Depending on its use it might be all events within a venue or just general list of events)
    const { venueId } = useParams()

    const [events, setEvents] = useState([])
    const [searchBarText, setSearchBarText] = useState('')

    const getEvents = async () => {
        // Gotta add search bar functionality for adding name queries here
        let response = venueId ? 
            await axios.get(`http://localhost:8000/venues/${venueId}/events`) : //This url will be changed once filtering is set up 
            await axios.get('http://localhost:8000/events')
        setEvents(response.data)
        console.log(response.data)
    }

    useEffect(() => {
        getEvents()
    }, [])
    
    return (
        <div className="eventListContainer">
            <SearchBar 
                searchBarText={searchBarText}
                setSearchBarText={setSearchBarText}
                onSubmit={getEvents}/>
            {
                events && events.map((event) => (
                    <EventListItem event={event} key={event.id}/>
                ))
            }
        </div>
    )
}