import { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate, useParams } from 'react-router-dom'

export default function VenueListItem () {
    const [venues, setVenues] = useState([])

    useEffect(() => {
        try {
            const response = axios.get(`localhost:8000/venues`)
            console.log(response)
            setVenues(response)
            console.log(venues)
        } catch (error) {
            console.error('Error fetching meal:', error)
        }
        
    }, [])

    return (
        <div><h3>helloe</h3></div>
    )
}