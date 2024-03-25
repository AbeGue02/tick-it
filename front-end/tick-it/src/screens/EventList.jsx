import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

export default function EventList() {
    // Lists all the events (Depending on its use it might be all events within a venue or just general list of events)
    const { venueId } = useParams()

    const [events, setEvents] = useState([])

    const getEvents = async () => {
        let response = await axios.get('')
        setEvents(response.data)
        console.log(response.data)
    }

    useEffect(() => {
        getEvents()
    }, [])
    
    return (
        <div>
            This is the EventList
        </div>
    )
}