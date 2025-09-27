```mermaid
%% Safe Path Hackathon - System Class Diagram
classDiagram
class SafePathApp {
    ```mermaid
    %% Safe Path Hackathon - System Class Diagram
    classDiagram
    class SafePathApp {
        + getLocation() Location
        + getDestination() Location
        + requestSafeRoute(Location, Location)
        + displayRoute(Route)
    }

    class SafePathAPI {
        + fetchCandidateRoutes(Location, Location) List<Route>
        + fetchSafetyData(Route) List<Incident>
        + computeSafetyScore(Route) float
        + chooseBestRoute(List<Route>) Route
    }

    class Route {
        + id: String
        + segments: List<Segment>
        + totalTime: int
        + riskScore: float
        + isSafe(): boolean
    }

    class Segment {
        + start: Location
        + end: Location
        + riskScore: float
        + incidents: List<Incident>
    }

    class Incident {
        + id: String
        + type: String
        + severity: int
        + timestamp: Date
        + location: Location
    }

    class Location {
        + latitude: float
        + longitude: float
        + address: String
    }

    class MapsAPI {
        + getRoutes(Location, Location) List<Route>
    }

    class CitizenAPI {
        + getIncidents(Location, radius: float) List<Incident>
    }

    SafePathApp --> SafePathAPI : requests safe route
    SafePathAPI --> MapsAPI : fetch routes
    SafePathAPI --> CitizenAPI : fetch incident data
    SafePathAPI --> Route : compute safety
    Route --> Segment : composed of
    Segment --> Incident : contains
    ```