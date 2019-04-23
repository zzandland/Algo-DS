#include "7_3.h"

int Music::n_musics_ = 0;
int Album::n_albums_ = 0;
int Artist::n_artists_ = 0;

Album::Album(std::string title, std::vector<Artist*> artists,
             Date released_date)
    : title_(title), artists_(artists), released_date_(released_date) {
  id_ = ++n_albums_;
};

Album::Album(std::string title, Artist artist, Date released_date)
    : title_(title), released_date_(released_date) {
  id_ = ++n_albums_;
  artists_.push_back(&artist);
};

Album::~Album() {
  for (Music* m : musics_) delete m;
};

void Album::AddMusic(Music* music) {
  musics_[music->GetTrackId()] = music;
  music->SetAlbum(this);
};

std::vector<Music*> Album::GetMusic() { return musics_; };

std::string Album::GetTitle() { return title_; };

int Album::GetReleasedYear() { return released_date_.year_; };
Artist::Artist(std::string first_name, std::string last_name, Date dob,
               std::map<int, std::vector<Album*>> albums)
    : first_name_(first_name),
      last_name_(last_name),
      dob_(dob),
      albums_(albums) {
  id_ = ++n_artists_;
};

Artist::~Artist() {
  for (auto it = albums_.begin(); it != albums_.end(); ++it) {
    for (Album* album : it->second) delete album;
  }
}

void Artist::AddAlbum(Album* album) {
  int released_year = album->GetReleasedYear();
  albums_[released_year].push_back(album);
};

std::vector<Album*> Artist::GetAllAlbums() {
  std::vector<Album*> output;
  for (auto it = albums_.begin(); it != albums_.end(); ++it)
    output.insert(output.end(), it->second.begin(), it->second.end());
  return output;
};

std::string Artist::GetFirstName() { return first_name_; };

std::string Artist::GetLastName() { return last_name_; };

Music::Music(std::string title, std::vector<Artist*> artists, int track_id,
             int duration, std::string genre, Date released_date)
    : track_id_(track_id),
      duration_(duration),
      title_(title),
      artists_(artists),
      genre_(genre),
      released_date_(released_date) {
  id_ = ++n_musics_;
  album_ = nullptr;
};

Music::Music(std::string title, Artist artist, int track_id, int duration,
             std::string genre, Date released_date)
    : track_id_(track_id),
      duration_(duration),
      title_(title),
      genre_(genre),
      released_date_(released_date) {
  id_ = ++n_musics_;
  artists_.push_back(&artist);
  album_ = nullptr;
};

std::string Music::GetTitle() { return title_; };

int Music::GetDuration() { return duration_; };

int Music::GetTrackId() { return track_id_; };

int Music::GetReleasedYear() { return released_date_.year_; };

void Music::SetAlbum(Album* album) { album_ = album; };

Jukebox::~Jukebox(){

};

void Jukebox::AddArtist(Artist* artist) {
  char first_char_art = artist->GetFirstName()[0];
  artists_[first_char_art].insert(artist);
  std::vector<Album*> albums = artist->GetAllAlbums();
  for (Album* album : albums) {
    char first_char_album = album->GetTitle()[0];
    albums_[first_char_album].insert(album);
    std::vector<Music*> musics = album->GetMusic();
    for (Music* music : musics) {
      char first_char_music = music->GetTitle()[0];
      musics_[first_char_music].insert(music);
    }
  }
};

void Jukebox::GetMusicByArtist(std::string artist) {
  char first_char = artist[0];
  std::set<Artist*> artist_set = artists_[first_char];
  for (auto it = artist_set.begin(); it != artist_set.end(); ++it) {
    if ((*it)->GetFirstName() == artist || (*it)->GetLastName() == artist) {
      std::vector<Album*> artist_album = (*it)->GetAllAlbums();
      for (Album* album : artist_album)
        for (Music* music : album->GetMusic()) {
          std::cout << music->GetTitle() << ", " << music->GetDuration() / 60
                    << ":" << music->GetDuration() % 60 << " // " << music->GetReleasedYear() << std::endl;
        }
    }
  }
  std::cout << "The artist is not found in the jukebox." << std::endl;
  return;
}

int main(void)
{
  
  return 0;
}
