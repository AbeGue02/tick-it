import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

export default function VenueDetails() {
    const { venueId } = useParams()
    const [venue, setVenue] = useState(null)

    useEffect(() => {
        const fetchVenue = async () => {
            try {
                let response = await axios.get(`http://localhost:8000/venues/${venueId}`)
                setVenue(response.data)
            } catch (error) {
                console.error('Error fetching venue details:', error)
            }
        }

        fetchVenue()
    }, [])

    if (!venue) return <div>Loading...</div>

    return (
        <div>
            <h2>Venue Details</h2>
            <h3>Name: {venue.name}</h3>
            <h4>Location: {venue.location}</h4>
        </div>
    )
}