import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

class Film {
    private String titre;
    private String description;
    private int likes;
    private int dislikes;

    public Film(String titre, String description) {
        this.titre = titre;
        this.description = description;
        this.likes = 0;
        this.dislikes = 0;
    }

    // Getters and setters for likes and dislikes

    public void like() {
        this.likes++;
    }

    public void dislike() {
        this.dislikes++;
    }

    // Other methods

    @Override
    public String toString() {
        return "Titre : " + titre + "\nDescription : " + description;
    }
}

class FilmRecommender {
    private List<Film> films;

    public FilmRecommender() {
        this.films = new ArrayList<>();
    }

    public void addFilm(Film film) {
        films.add(film);
    }

    public List<Film> getTopFilms(int count) {
        return films.stream()
                .sorted(Comparator.comparingInt(Film::getLikes).reversed())
                .limit(count)
                .collect(Collectors.toList());
    }

    public List<Film> searchFilms(String keyword) {
        return films.stream()
                .filter(film -> film.getTitre().toLowerCase().contains(keyword.toLowerCase()))
                .collect(Collectors.toList());
    }
}

public class Main {
    public static void main(String[] args) {
        FilmRecommender recommender = new FilmRecommender();

        // Ajouter des films à la base de données
        recommender.addFilm(new Film("Film 1", "Description du film 1"));
        recommender.addFilm(new Film("Film 2", "Description du film 2"));
        recommender.addFilm(new Film("Film 3", "Description du film 3"));

        // Afficher la liste de tous les films
        List<Film> allFilms = recommender.getTopFilms(100);
        for (Film film : allFilms) {
            System.out.println(film);
        }

        // Rechercher des films par nom
        String keyword = "Film 1";
        List<Film> searchResults = recommender.searchFilms(keyword);
        for (Film film : searchResults) {
            System.out.println(film);
        }

        // Afficher les détails d'un film
        Film filmDetails = allFilms.get(0);
        System.out.println(filmDetails);

        // Liker ou disliker un film
        filmDetails.like();
        filmDetails.like();
        filmDetails.dislike();

        // Afficher les films triés par pertinence en fonction des likes
        List<Film> topFilms = recommender.getTopFilms(10);
        for (Film film : topFilms) {
            System.out.println(film);
        }
    }
}
