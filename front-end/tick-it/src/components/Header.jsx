import { useNavigate } from "react-router-dom"
import { Link } from 'react-router-dom'

export default function Header() {
    // Contains buttons to venues and event screens
    
    let navigate = useNavigate()

    return (
        <header className="headerContainer">
            <Link to='/' className='home-button'>
            <h1>Tick-IT</h1>
            </Link>
            <nav>
            <Link to='/venues' className='venue-button'><button onClick={() => navigate('/venues')}>Venues</button></Link>
            <Link to='/events' className='event-button'><button>Events</button></Link>
            </nav>
        </header>
    )
}