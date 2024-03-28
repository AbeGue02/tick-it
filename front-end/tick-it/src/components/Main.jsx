import { Routes, Route } from 'react-router-dom'
import VenueList from '../screens/VenueList'
import EventList from '../screens/EventList'
import Home from '../screens/Home'
import EventDetails from '../screens/EventDetails'
import VenueDetails from '../screens/VenueDetails'
import Checkout from './Checkout'

export default function Main() {
    return (
        <>
            <Routes>
                <Route path='/' element={<Home/>}/>
                <Route path='/venues' element={<VenueList/>}/>
                <Route path='/venues/:venueId' element={<VenueDetails/>}/>
                <Route path='/venues/:venueId/events' element={<EventList/>}/>
                <Route path='/events' element={<EventList/>}/>
                <Route path='/events/:eventId' element={<EventDetails/>}/>
                <Route path='/checkout' element={<Checkout/>}/>
            </Routes>
        </>
    )
}