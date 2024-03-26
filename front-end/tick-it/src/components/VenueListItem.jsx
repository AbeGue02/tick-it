import { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate, useParams } from 'react-router-dom'

export default function VenueListItem () {
    const [venues, setVenues] = useState([])

    useEffect(() => {
        try {
            const response = axios.get(`localhost:8000/locations`)
            console.log(response)
            setVenues(response)
            console.log(venues)
        } catch (error) {
            console.error('Error fetching meal:', error)
        }
        
    }, [])

    return (
        <div>
        <ul>
            {props.venues.map(venue => (
                <div className='venueListItemContainer'>
                <h3>{venue.name}</h3>
                <h4>{venue.location}</h4>
                </div>
            ))}
        </ul>
        </div>
    )
}