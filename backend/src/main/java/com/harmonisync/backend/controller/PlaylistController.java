package com.harmonisync.backend.controller;

import com.harmonisync.backend.model.TrackMetadata;
import org.springframework.core.io.FileSystemResource;
import org.springframework.http.*;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;

@RestController
@RequestMapping("/api")
public class PlaylistController {

    private final RestTemplate restTemplate = new RestTemplate();
    private static final String ANALYZER_URL = "http://localhost:6000/analyze";

    @PostMapping("/upload")
    public ResponseEntity<TrackMetadata> uploadTrack(@RequestParam("file") MultipartFile file) {
        try {
            File tempFile = File.createTempFile("track-", file.getOriginalFilename());
            file.transferTo(tempFile);

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.MULTIPART_FORM_DATA);

            MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
            body.add("file", new FileSystemResource(tempFile));

            HttpEntity<MultiValueMap<String, Object>> requestEntity = new HttpEntity<>(body, headers);

            ResponseEntity<TrackMetadata> response = restTemplate.postForEntity(
                    ANALYZER_URL,
                    requestEntity,
                    TrackMetadata.class);

            tempFile.delete();
            return response;

        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }
}
