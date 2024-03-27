import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'
import VenueListItem from '../components/VenueListItem'

export default function VenueList() {
    const [venues, setVenues] = useState([])
    const { venueId } = useParams()
    const [events, setEvents] = useState([])
    const [searchBarText, setSearchBarText] = useState('')

    const fetchVenues = async () => {
        let response = await axios.get('http://localhost:8000/venues')
        setVenues(response.data)
    }

    useEffect(() => {
        fetchVenues()
    }, [])

    // const getEvents = async () => {
    //     let response;
    //     if (venueId) {
    //         response = await axios.get(`http://localhost:8000/venues/${venueId}`)
    //     } else {
    //         response = await axios.get('http://localhost:8000/events')
    //     }
    //     venueId 
    //     ? setEvents(searchBarText ? response.data.event.filter((event) => event.name.includes(searchBarText)) : response.data.event)
    //     : setEvents(searchBarText ? response.data.filter((event) => event.name.includes(searchBarText)) : response.data)
    //     console.log(response.data)
    // }

    // useEffect(() => {
    //     getEvents();
    // }, [venueId]); // Fetch events whenever venueId changes

    return (
        <div>
            {venues.map((venue) => (
                <VenueListItem key={venue.id} venue={venue} />
            ))}
        </div>
    )
}